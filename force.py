import threading
import time
from encryption import encrypt
from decryption import decrypt


class BruteForceDecrypt:
    def __init__(self):
        self.correct_keys = []
        self.lock = threading.Lock()

    def _brute_force(self, pairs, start, end):
        for key in range(start, end):
            key_str = '{0:010b}'.format(key)
            for plaintext, ciphertext in pairs:
                decrypted = decrypt(ciphertext, key_str)
                if decrypted != plaintext:
                    break
            else:
                with self.lock:
                    if len(key_str) == 10:
                        self.correct_keys.append(key_str)

    def single_thread_brute_force(self, pairs):
        self._brute_force(pairs, 0, 2 ** 10)
        return self.correct_keys

    def multi_thread_brute_force(self, pairs):
        threads = []
        for i in range(8):
            start = i * (2 ** 9)
            end = (i + 1) * (2 ** 9)
            thread = threading.Thread(target=self._brute_force, args=(pairs, start, end))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return self.correct_keys

    def decrypt(self, plaintext_str, ciphertext_str):
        # Split the input strings into lists of plaintexts and ciphertexts
        plaintexts = plaintext_str.split(";")
        ciphertexts = ciphertext_str.split(";")

        # Zip the plaintexts and ciphertexts together to create pairs
        pairs = list(zip(plaintexts, ciphertexts))

        # Single-threaded brute force
        start_time = time.time()
        single_result = self.single_thread_brute_force(pairs)
        single_time = time.time() - start_time
        self.correct_keys.clear()  # Reset for the next brute force

        # Multi-threaded brute force
        start_time = time.time()
        multi_result = self.multi_thread_brute_force(pairs)
        multi_time = time.time() - start_time

        return {
            "single_thread": {
                "keys": single_result,
                "time": single_time
            },
            "multi_thread": {
                "keys": multi_result,
                "time": multi_time
            }
        }
