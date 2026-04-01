import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def call_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# -------------------------------
# SQL GENERATION
# -------------------------------
def generate_sql(question):

    prompt = f"""
You are an expert SQL generator using DuckDB.

STRICT RULES:
- ONLY return SQL
- NO explanation
- NO markdown
- NO extra text

DATABASE SCHEMA:

TABLE: pos_transactions (pt)
- sku_code
- gross_sales_gbp

TABLE: wms_sku_mapping (ws)
- wms_sku_code
- canonical_sku_id

TABLE: product_master (pm)
- sku_id
- brand_name
- list_price_gbp
- cogs_gbp

CORRECT JOIN LOGIC (MANDATORY):

- DEFAULT JOIN (MANDATORY):
  pos_transactions.sku_code = product_master.sku_id

- DO NOT USE wms_sku_mapping unless explicitly required.
- NEVER introduce unnecessary joins.
- NEVER hallucinate columns.

NEVER:
- DO NOT use pt.sku_id (does NOT exist)
- DO NOT skip wms_sku_mapping
- DO NOT invent columns

BUSINESS LOGIC:
- revenue = SUM(pt.gross_sales_gbp)
- margin = (pm.list_price_gbp - pm.cogs_gbp) / pm.list_price_gbp

EXAMPLES:

Q: top 5 brands by revenue
SQL:
SELECT pm.brand_name,
SUM(pt.gross_sales_gbp) AS revenue
FROM pos_transactions pt
JOIN wms_sku_mapping ws ON pt.sku_code = ws.wms_sku_code
JOIN product_master pm ON ws.canonical_sku_id = pm.sku_id
GROUP BY pm.brand_name
ORDER BY revenue DESC
LIMIT 5;

Q: highest margin brand
SQL:
SELECT pm.brand_name,
AVG((pm.list_price_gbp - pm.cogs_gbp) / pm.list_price_gbp) AS avg_margin
FROM product_master pm
GROUP BY pm.brand_name
ORDER BY avg_margin DESC
LIMIT 1;

Now generate SQL:

Q: {question}
"""

    sql = call_ollama(prompt)

    # CLEAN OUTPUT (very important)
    sql = sql.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


# -------------------------------
# INSIGHT GENERATION
# -------------------------------
def generate_insight(df, question):

    # ---- safety checks ----
    if df is None:
        return "No data available to generate insights."

    if isinstance(df, str):
        return "No data available to generate insights."

    try:
        if len(df) == 0:
            return "No data available to generate insights."
    except:
        return "No data available to generate insights."

    # ---- convert df safely ----
    try:
        sample = df.head(10).to_string(index=False)
    except:
        return "No data available to generate insights."

    prompt = f"""
You are a business analyst.

Question:
{question}

Data:
{sample}

Give:
1. Key Insight
2. Business Meaning

Be concise and factual.
"""

    return call_ollama(prompt)