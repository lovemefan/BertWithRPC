# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 9:47
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : rpc.py
import pickle

from tzrpc.proto.py.Boolean_pb2 import Boolean
from tzrpc.proto.py.Bytes_pb2 import Bytes
from tzrpc.proto.py.Number_pb2 import Double, Float, Integer
from tzrpc.proto.py.Numpy_pb2 import ndarrays
from tzrpc.proto.py.String_pb2 import String
from tzrpc.utils.logger import get_logger
from tzrpc.utils.numpy_serialized import numpy2protobuf, protobuf2numpy

servicers = []

logger = get_logger(to_std=True, stdout_level="INFO", save_log_file=False)


class RpcServicer:
    def __init__(self):
        pass

    def register(self, task):
        _listener = Listener(task)
        # print(_listener)
        logger.debug(f"Instance's task  {_listener.task} registered")
        servicers.append(_listener)

        def wrapper(*args, **kwargs):
            print(args, kwargs)
            print(f"{task.__name__}: text")
            self.args = args
            self.kwargs = kwargs
            return task(*args, **kwargs)

        return wrapper


class Listener:
    def __init__(self, task):
        logger.info(f"Method {task} {task.__name__}() registered.")
        self.task = task
        logger.debug(f"self Method {self.task} {task.__name__}() registered.")

    def wrapper(self, *args, **kwargs):
        print(args, kwargs)
        print(f"{self.task.__name__}: text")
        return self.task(*args, **kwargs)

    def toString(self, request, context):
        logger.debug(f"Method toString({request}) called.")
        result = self.task(request.text)
        response = String(text=result)
        return response

    def toInteger(self, request, context):
        logger.debug(f"Method toInteger({request}, {context}) called.")
        result = self.task(request.value)
        response = Integer(value=result)
        return response

    def toFloat(self, request, context):
        logger.debug(f"Method toFloat({request}, {context}) called.")
        result = self.task(request.value)
        response = Float(value=result)
        return response

    def toDouble(self, request, context):
        logger.debug(f"Method toDouble({request}, {context}) called.")
        result = self.task(request.value)
        response = Double(value=result)
        return response

    def toBoolean(self, request, context):
        logger.debug(f"Method toBoolean({request}, {context}) called.")
        result = self.task(request.value)
        response = Boolean(value=result)
        return response

    def toBytes(self, request, context):
        logger.debug(f"Method toBytes({request}, {context}) called.")
        data = request.data
        is_pickled = True if b"PICKLE" in data[:6] else False

        if is_pickled:
            data = pickle.loads(data[6:])
        result = self.task(data)
        if is_pickled:
            result = pickle.dumps(result)
        response = Bytes(data=result)
        return response

    def toNdarray(self, request, context):
        logger.debug(f"Method toNdarray({request}) called.")
        value = protobuf2numpy(request)
        data = self.task(value)
        response = numpy2protobuf(data)
        return response

    def toNdarrays(self, request, context):
        logger.debug(f"Method toNdarrays({request}) called.")
        _ndarray = self.task(request.value)
        response = ndarrays(ndarray=_ndarray)
        return response

    def toTensor(self, request, context):
        pass

    def toTensors(self, request, context):
        pass

    def toIntegerArrayList(self, request, context):
        pass

    def toFloatArrayList(self, request, context):
        pass

    def toDoubleArrayList(self, request, context):
        pass

    def toBooleanArrayList(self, request, context):
        pass
