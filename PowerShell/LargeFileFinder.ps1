﻿gci -r| sort -Descending -Property length | select -First 10 name, @{Name ="Gigabytes";Expression={[Math]::Round($_.length / 1GB, 2)}}