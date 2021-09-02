import threading
import time
import logging
import sys
import functools
import inspect
import uuid


class Progress:
    def __init__(self, th_name: str = str(uuid.uuid4())):
        """
        Constructor method
        Initialize _execute -> required to control the lifecycle of a thread.
            _execute -> private to Progress class
        Initialize logger -> required for logging
        :param th_name: str -> unique thread name auto-generated
            if nothing passed as argument.
        """
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.INFO)
        self._logger.addHandler(logging.StreamHandler(sys.stdout))
        self._is_running = False
        self.th_name = th_name

    def _stop(self) -> None:
        """
        Method used for terminating a thread.
        Sets the variable _execute to False
        :return: None
        """
        self._is_running = False

    @staticmethod
    def get_caller_func() -> str:
        """
        Method is used mainly while logging, can exactly point to the class
            and method from where an event has occurred.
        :return: class name and the method name from where get_caller was called.
        :rtype: str
        """
        stack = inspect.stack()
        from_class = stack[1][0].f_locals["self"].__class__.__name__
        from_method = stack[1][0].f_code.co_name
        return "[{}.{}] - ".format(from_class, from_method)

    def _run(self, caller_func: str, max_timeout: int, log_interval: int = 2) -> None:
        """
        Method used for managing a thread and monitoring the progress.
        Runs this method till _is_running is set to False or implicit Timeout
            based on the given params
        :param caller_func: str -> parent function name from which _run was invoked
        :param max_timeout: int -> time after which thread is terminated
        :param log_interval: int -> interval at which progress is logged
        :return: None
        """
        at_iter: int = 0
        max_iteration = max_timeout/log_interval
        while self._is_running and at_iter < max_iteration:
            at_iter += 1
            log = "#" * at_iter
            self._logger.info(f"[{caller_func}._is_running] - {log}")
            if at_iter >= max_iteration - 1:
                self._logger.warning(f"[tracker.is_terminated] - "
                                     f"Progress Tracker Timed out! {caller_func} is still running...")
                return
            time.sleep(log_interval)
            if not self._is_running:
                self._logger.info(f"[{caller_func}._is_done] - {log}!")
                return

    def tracker(self, max_timeout: int = 18000, log_interval: int = 2):
        """
        Decorator which tracks progress of the parent function.
        :param max_timeout: int
        :param log_interval: int
        :return: parent method data
        """
        def track(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                self._is_running = True
                caller_func = f"{func.__name__}"
                th = threading.Thread(target=self._run,
                                      args=(caller_func, max_timeout, log_interval),
                                      name=self.th_name)
                th.start()
                output = func(*args, **kwargs)
                self._stop()
                th.join()
                return output

            wrapper.is_running = False
            return wrapper

        return track
