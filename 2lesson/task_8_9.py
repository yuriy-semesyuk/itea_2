from datetime import datetime, timedelta
from time import sleep

cached_dic = {}


def cached(*dec_args, **dec_kwargs):
    def wrraper(func):
        def inner(*args, **kwargs):
            if args in cached_dic and (datetime.now() - cached_dic[args]["time"]) < \
                    timedelta(seconds=dec_kwargs["second"]):
                return "{} {}".format(cached_dic[args]["cache_result"], "cached")
            else:
                cached_dic[args] = {"cache_result": func(*args, **kwargs), "time": datetime.now()}
            return cached_dic[args]["cache_result"]
        return inner
    return wrraper


@cached(second=5)
def add_cached(*args):
    return sum(args)


if __name__ == "__main__":
    print(add_cached(12, 17, 45))
    sleep(5)
    print(add_cached(12, 17, 45))
    print(add_cached(122, 117, 42))
    sleep(5)
    print(add_cached(12, 17, 45))
    print(add_cached(122, 117, 42))
