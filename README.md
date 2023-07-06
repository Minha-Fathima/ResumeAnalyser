# Re-Check: Resume Analyser

# Description
Re-Check scans resumes and provides personalized recommendations for skills and certification. 
Moreover, It fixes grammatical errors to enhance your resume even further!

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
