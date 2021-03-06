from typing import Tuple, Any, Dict, Type
import tensorflow as tf
from tensorflow import Tensor
import numpy as np

from decompose.distributions.distribution import DrawType, UpdateType
from decompose.distributions.distribution import Distribution
from decompose.distributions.nnNormal import NnNormal
from decompose.distributions.distribution import parameterProperty
from decompose.distributions.algorithms import Algorithms
from decompose.distributions.cenNnNormalAlgorithms import CenNnNormalAlgorithms


class CenNnNormal(NnNormal):
    def __init__(self,
                 tau: Tensor = tf.constant([1.]),
                 name: str = "NA",
                 algorithms: Type[Algorithms] = CenNnNormalAlgorithms,
                 drawType: DrawType = DrawType.SAMPLE,
                 updateType: UpdateType = UpdateType.ALL,
                 persistent: bool = True) -> None:
        Distribution.__init__(self,
                              shape=tau.shape,
                              latentShape=(),
                              name=name,
                              algorithms=algorithms,
                              drawType=drawType,
                              dtype=tau.dtype,
                              updateType=updateType,
                              persistent=persistent)
        self._init({"tau": tau})

    @staticmethod
    def initializers(shape: Tuple[int, ...] = (1,),
                     latentShape: Tuple[int, ...] = (),
                     dtype: np.dtype = np.float32) -> Dict[str, Tensor]:
        initializers = {
            "tau": tf.constant(np.random.exponential(size=shape), dtype=dtype)
        }  # type: Dict[str, Tensor]
        return(initializers)

    @property
    def mu(self) -> Tensor:
        mu = tf.zeros_like(self.tau)
        return(mu)

    @parameterProperty
    def tau(self) -> Tensor:
        return(self.__tau)

    @tau.setter("tau")
    def tau(self, tau: Tensor):
        self.__tau = tau
