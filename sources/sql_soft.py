sql_injections_soft_check = (
    "drop",
    "--",
    "table",
    "users",
    "1=1",
    "or",
    "admin",
    "from",
    "exec",
    "xp_cmdshell",
)