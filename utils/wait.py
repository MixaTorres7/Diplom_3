import time


def wait_until(driver, timeout, condition):
    """Ожидание: проверяет condition каждые 0.5 сек до timeout."""
    end = time.time() + timeout
    while time.time() < end:
        try:
            result = condition(driver)
            if result:
                return result
        except Exception:
            pass
        time.sleep(0.5)
    raise TimeoutError(f'ожидание {timeout} сек истекло')
