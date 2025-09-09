CASE WHEN days_since_last_login < 30 THEN TRUE ELSE FALSE END AS is_active,
CASE WHEN total_spent < 100 THEN TRUE ELSE FALSE END AS low_spender,
CASE WHEN support_tickets_last_90d = 0 THEN TRUE ELSE FALSE END AS no_recent_support