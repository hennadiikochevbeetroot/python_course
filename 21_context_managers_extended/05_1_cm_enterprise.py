import selenium
from contextlib import contextmanager


@contextmanager
def create_driver(disable_gpu: bool = True):
    driver = selenium.WebDriver(
        window_size='1200x900',
        disable_gpu=disable_gpu,
    )

    driver.download_directory = '/Downloads'

    try:
        yield driver
    finally:
        driver.stop()
        driver.close()


class CreateDriver:
    def __init__(self):
        self.driver = selenium.WebDriver(
            window_size='1200x900',
            disable_gpu=disable_gpu,
        )
        self.specify_driver_options()

    def specify_driver_options(self):
        self.driver.download_directory = '/Downloads'
        ...

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.stop()
        self.driver.close()


with create_driver() as driver:
    driver.execute_script()
    driver.press_button()

