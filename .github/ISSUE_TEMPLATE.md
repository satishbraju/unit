---
title: Issue based on Push or PR
assignees: satishbraju, satishbettadapur
labels: bug, enhancement
---
Someone just pushed, oh no! Here's who did it: {{ payload.sender.login }}.
Created issue number ${{ steps.create-issue.outputs.number }}