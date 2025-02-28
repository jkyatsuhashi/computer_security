# DES Algorithm Constants
KEY_COMPRESSION_TABLE_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

KEY_COMPRESSION_TABLE_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

ROTATION_AMOUNTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

INITIAL_PERMUTATION = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

EXPANSION_TABLE = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 
         16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

SUBSTITUTION_BOXES = [
    # Box 1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # Box 2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # Box 3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # Box 4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # Box 5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # Box 6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # Box 7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # Box 8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

PERMUTATION_TABLE = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

FINAL_PERMUTATION = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


class DataEncryptionStandardCipher:
    """
    Implementation of the Data Encryption Standard (DES) decryption algorithm
    """
    def __init__(self, encryption_key, encrypted_data):
        self.encryption_key = encryption_key
        self.encrypted_data = encrypted_data
        self.subkeys = []
        
    def apply_permutation(self, bit_string, permutation_map):
        """
        Rearranges bits according to specified permutation map
        
        """
        return ''.join(bit_string[i-1] for i in permutation_map)
        
    def circular_shift(self, bit_string, positions):
        """
        Rotates the bits to the left by the specified number of positions

        """
        return bit_string[positions:] + bit_string[:positions]
        
    def binary_xor(self, string_a, string_b):
        """
        Performs bitwise XOR operation on two bit strings
        

        """
        return ''.join(str(int(a) ^ int(b)) for a, b in zip(string_a, string_b))
    
    def create_subkeys(self):
        """
        Generates 16 subkeys needed for DES encryption/decryption process

        """
        # Apply first compression permutation
        compressed_key = self.apply_permutation(self.encryption_key, KEY_COMPRESSION_TABLE_1)
        
        # Split the 56-bit key into two 28-bit halves
        left_block = compressed_key[:28]
        right_block = compressed_key[28:]
        
        # Store all versions of the key halves
        left_block_series = [left_block]
        right_block_series = [right_block]
        
        # Generate all rotated versions of key halves
        for shift_amount in ROTATION_AMOUNTS:
            left_block = self.circular_shift(left_block, shift_amount)
            right_block = self.circular_shift(right_block, shift_amount)
            left_block_series.append(left_block)
            right_block_series.append(right_block)
        
        # Create 16 subkeys by combining and compressing the key halves
        for i in range(1, 17):
            combined_block = left_block_series[i] + right_block_series[i]
            self.subkeys.append(self.apply_permutation(combined_block, KEY_COMPRESSION_TABLE_2))
            
        return self.subkeys
    
    def apply_substitution(self, expanded_bits):
        """
        Applies S-box substitution to transform 48 bits into 32 bits

        """
        output_bits = ""
        
        # Process each 6-bit segment
        for box_num in range(8):
            # Extract current 6-bit segment
            current_segment = expanded_bits[box_num*6:(box_num+1)*6]
            
            # Calculate row and column indices for S-box
            row_index = int(current_segment[0] + current_segment[5], 2)
            column_index = int(current_segment[1:5], 2)
            
            # Look up value in appropriate S-box
            s_box_value = SUBSTITUTION_BOXES[box_num][row_index][column_index]
            
            # Convert to 4-bit binary and append
            output_bits += format(s_box_value, '04b')
            
        return output_bits
    
    def feistel_function(self, block, subkey):
        """
        Implements the core Feistel function used in each round

        """
        # Expand block from 32 to 48 bits
        expanded_block = self.apply_permutation(block, EXPANSION_TABLE)
        
        # XOR with the subkey
        mixed_block = self.binary_xor(expanded_block, subkey)
        
        # Apply S-box substitution (48 bits -> 32 bits)
        substituted_block = self.apply_substitution(mixed_block)
        
        # Apply final permutation in the function
        return self.apply_permutation(substituted_block, PERMUTATION_TABLE)
    
    def decrypt(self, debug=True):
        """
        Performs full DES decryption process
        
        """
        # Generate all subkeys for decryption
        self.create_subkeys()
        
        # Print subkeys if debugging
        if debug:
            for i, key in enumerate(self.subkeys):
                print(f"Subkey {i+1}: {key}")
        
        # Initial permutation of ciphertext
        current_block = self.apply_permutation(self.encrypted_data, INITIAL_PERMUTATION)
        
        # Split block into left and right halves
        left_half = current_block[:32]
        right_half = current_block[32:]
        
        # Apply 16 rounds of decryption in reverse order
        for round_num in range(15, -1, -1):
            # Store current right half
            temp = right_half
            
            # Apply Feistel function and XOR with left half
            transformed_block = self.feistel_function(right_half, self.subkeys[round_num])
            right_half = self.binary_xor(left_half, transformed_block)
            
            # Update left half
            left_half = temp
            
            # Print state after each round if debugging
            if debug:
                print(f"Iteration {16-round_num}: {left_half + right_half}")
        
        # Apply final permutation (swap left and right first)
        decrypted_result = self.apply_permutation(right_half + left_half, FINAL_PERMUTATION)
        
        if debug:
            print(f"Decrypted: {decrypted_result}")
        
        return decrypted_result


# Test the implementation
if __name__ == "__main__":
    # Original test data
    encryption_key = "0100110001001111010101100100010101000011010100110100111001000100"
    encrypted_text = "1100101011101101101000100110010101011111101101110011100001110011"
    
    # Create cipher object
    des_cipher = DataEncryptionStandardCipher(encryption_key, encrypted_text)
    
    # Execute decryption
    plaintext = des_cipher.decrypt()