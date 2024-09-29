import random
# pip3 install mersenne-twister-predictor
from mt19937predictor import MT19937Predictor

predictor = MT19937Predictor()

for _ in range(624):
    x = random.getrandbits(32)
    predictor.setrandbits(x, 32)  # Submit samples here

# When enough samples are given, you can start predicting:
assert random.getrandbits(32) == predictor.getrandbits(32)