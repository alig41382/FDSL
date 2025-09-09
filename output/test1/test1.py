df["is_active"] = (df["days_since_last_login"] < 30)
df["low_spender"] = (df["total_spent"] < 100)
df["no_recent_support"] = (df["support_tickets_last_90d"] == 0)