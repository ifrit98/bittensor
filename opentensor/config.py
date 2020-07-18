from loguru import logger

import argparse
import requests
import random

import opentensor

class Config:
    
    def __init__(self, hparams):
        self._hparams = hparams
        self._load_defaults()
        self.toString()
    
    def toString(self):
        logger.info("\n Neuron key: {} \n Axon port: {} \n Metagraph port: {} \n Metagraph Size: {} \n bootpeer: {} \n remote_ip: {} \n", self.identity.public_key(), self.axon_port, self.metagraph_port, self.metagraph_size, self.bootstrap, self.remote_ip)
    
    def _load_defaults(self):
        # Fall back on random port for axon bind. 
        if self._hparams.axon_port == None:
            self.axon_port = str(random.randint(6000, 60000))
        else:
            self.axon_port = self._hparams.axon_port
        
        # Fall back on random port for metagraph bind.
        if self._hparams.metagraph_port == None:
            self.metagraph_port = str(random.randint(6000, 60000))
        else:
            self.metagraph_port = self._hparams.metagraph_port
        
        # Fall back to default.
        # TODO(const) checks.
        self.metagraph_size = self._hparams.metagraph_size
        
        # Fallback on common boot peer if otherwise not set.
        if self._hparams.bootstrap == None:
            self.bootstrap = "165.227.216.95:8080"
        else:
            self.bootstrap = self._hparams.bootstrap
          
        # Fall back on creating new identity.   
        if self._hparams.identity == None:
            self.identity = opentensor.Identity()
        else:
            # TODO(const) load identity from public key.
            pass
            
        if self._hparams.remote_ip == None:
            self.remote_ip = requests.get('https://api.ipify.org').text
        else:
            self.remote_ip = self._hparams.remote_ip

    
    @staticmethod
    def add_args(parser: argparse.ArgumentParser):
        parser.add_argument('--chain_endpoint',
                        default=None,
                        type=str,
                        help="bittensor chain endpoint.")
        parser.add_argument('--axon_port',
                        default=None,
                        type=str,
                        help="Axon terminal bind port")
        parser.add_argument('--metagraph_port',
                        default=None,
                        type=str,
                        help="Metagraph bind port.")
        parser.add_argument('--metagraph_size',
                            default=100000,
                            type=int,
                            help='Metagraph cache size.')
        parser.add_argument('--bootstrap',
                            default=None,
                            type=str,
                            help='Metagraph bootpeer')
        parser.add_argument('--identity',
                            default=None,
                            type=str,
                            help='Identity')
        parser.add_argument('--remote_ip',
                            default=None,
                            type=str,
                            help='Remote serving ip.')
        return parser