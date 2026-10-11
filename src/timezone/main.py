import platform
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

if platform.system() == "Windows":
    from tzlocal.windows_tz import win_tz

    timezone_id = subprocess.check_output(
        ["powershell", "-NoProfile", "-Command", "(Get-TimeZone).Id"],
        text=True,
    ).strip()
    timezone = ZoneInfo(win_tz[timezone_id])
else:
    with Path("/etc/localtime").open("rb") as file:
        timezone = ZoneInfo.from_file(file)

now = datetime.now(timezone)
offset = now.strftime("%z")
print(f"{now.tzname()} UTC{offset[:-2]}:{offset[-2:]}")