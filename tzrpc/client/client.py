# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 21:41
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : client.py
import logging
import numbers
import pickle

import grpc
import numpy as np

from tzrpc.proto.py.Boolean_pb2 import Boolean
from tzrpc.proto.py.Bytes_pb2 import Bytes
from tzrpc.proto.py.Number_pb2 import Double, Integer
from tzrpc.proto.py.Server_pb2_grpc import toObjectStub
from tzrpc.proto.py.String_pb2 import String
from tzrpc.utils.constant import MAX_MESSAGE_LENGTH
from tzrpc.utils.logger import get_logger
from tzrpc.utils.numpy_serialized import numpy2protobuf, protobuf2numpy

logger = get_logger(to_std=True, stdout_level="INFO", save_log_file=False)

try:
    import torch
except ImportError:
    print(
        "if you want use torch, please install torch with command `pip install torch` "
    )


class TZPRC_Client:
    __type = [str, np.ndarray, bytes, numbers.Number, bool]
    tensor_type = None
    try:
        import torch

        tensor_type = torch.Tensor
        __type.append(torch.Tensor)
    except ImportError:
        logger.info(
            """
        Please pip install torch to get tensor support
        """
        )

    def __init__(self, server_address: str, debug=False):
        if debug:
            logger.setLevel(logging.DEBUG)
        self.server_address = server_address
        self.channel = grpc.insecure_channel(server_address,
                                             options=[('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                                                      ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)]
                                             )

    def register(self, func):
        """
        :param return_type: type of return [String, ]
        :return:
        """
        # if return_type not in self.__type:
        #     raise ValueError(f"TZRPC return type only support {self.__type}")

        def wrapper(*args, **kwargs):
            stub = toObjectStub(self.channel, func.__name__)
            result = func(*args, **kwargs)
            if isinstance(result, str):
                request = String(text=result)
                response = stub.toString(request).text

            elif isinstance(result, np.ndarray):
                request = numpy2protobuf(result)
                response = protobuf2numpy(stub.toNdarray(request))
            elif isinstance(result, bytes):
                request = Bytes(data=result)
                response = stub.toBytes(request).data
            elif isinstance(result, bool):
                request = Boolean(value=result)
                response = bool(stub.toBoolean(request).value)
            elif isinstance(result, numbers.Number):
                if isinstance(result, int):
                    request = Integer(value=result)
                    response = stub.toInteger(request).value
                elif isinstance(result, float):
                    request = Double(value=result)
                    response = stub.toDouble(request).value
                else:
                    logger.exception(f"Type of {type(result)} is not support")
            elif self.tensor_type is not None and isinstance(result, self.tensor_type):
                request = numpy2protobuf(result.numpy())
                response = torch.from_numpy(
                    protobuf2numpy(stub.toNdarray(request)).copy()
                )
            else:
                logger.info(f"Data will serialized by pickle and send with bytes")
                obj = pickle.dumps(result)
                request = Bytes(data=b"PICKLE"+obj)
                response = pickle.loads(stub.toBytes(request).data)
                logger.debug(f"type of data loaded is {type(response)}")

            return response

        return wrapper
