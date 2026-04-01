def run_query(conn, sql):
    try:
        df = conn.execute(sql).fetchdf()
        return df, None
    except Exception as e:
        return None, str(e)