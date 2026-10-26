# The Royal Card availability

Checks only the publicly available API health endpoint and landing page every ten minutes, with three attempts before a failure. No app source, personal information or credentials are included. Standard GitHub-hosted runners for this public repository are free.

Failures open one GitHub issue; recovery closes it. The operator watches this repository for notifications. Delivery by email depends on the operator's personal GitHub notification settings. Scheduled runs may be delayed; this is a basic launch monitor, not an SLA. Monthly maintenance records repository activity to prevent the normal 60-day public-schedule inactivity suspension. Check the Actions history periodically; GitHub itself is not covered by this monitor.

Run manually: `python3 check.py` or Actions → Availability → Run workflow.
