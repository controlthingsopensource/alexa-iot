# Alexa skill
## About 
A sample alexa skill for interacting with your IoT device.

## Preparation
Update `lambda\lambda_function.py`,  line 50, with your IoT device URL. Compress the skill
and upload it to you Amazon developer console

## Execution
Deploy the skill and in the `Test` section say (or type):

```
open invoke
```

The skill will respond with `Welcome, you can say execute hello, followed by a word.`. Then say (or type):

```
execute hello admin
```