# Re-Check: Resume Analyser
Scan you resume and receive personalized recommendations for skills and certification. Moreover, fix you grammatical issues to enhance your resume even further!

# How to run
1. Create a .env in the given format inside botcore/

```
AI21=ai_key
LANGCHAIN=langchain_plus_key
```
2. To import botcore/

```python
# ./tests/test_ai21.py

import sys
import os

# should point to the parent folder of botcore
sys.path.append(f'{os.path.dirname(__file__)}/../')

from botcore.setup import trace_ai21

MODEL = trace_ai21()
```
