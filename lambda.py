import time

def lambda_handler(event, context):
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Your code that might fail
            result = do_something(event)
            return result
        except Exception as e:
            retry_count += 1
            time.sleep(2**retry_count)  # Exponential backoff
            continue

    # If all retries fail, you can log or send to a DLQ or take other actions.
