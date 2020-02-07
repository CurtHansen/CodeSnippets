from string import ascii_lowercase, ascii_uppercase

all_letters = ascii_lowercase + ascii_uppercase


class TreeNode(object):
    def __init__(self, x=None, t=False):
        self.value = x
        self.terminus = t
        self.children = [None] * 52


def findSubstrings(words, parts):

    def add_part_to_trie(snippet, root_node):
        len_snippet = len(snippet)

        def recur_process_letter_in_current_node(pos, current_node):
            current_letter = snippet[pos]
            letter_index = all_letters.index(current_letter)
            if current_node.children[letter_index]:
                current_node = current_node.children[letter_index]
            else:
                new_node = TreeNode(pos + 1)
                current_node.children[letter_index] = new_node
                current_node = new_node
            if pos < len_snippet - 1:
                recur_process_letter_in_current_node(pos + 1, current_node)
            if pos == len_snippet - 1:
                current_node.terminus = True

        recur_process_letter_in_current_node(0, root_node)

    def process_word(inword):

        longest_match_for_word = 0
        result = inword

        def search_trie_from_word_pos(starting_pos_in_word):
            max_match_length = 0
            cumulative_match_length = 0

            def recur_search_trie(current_trie_node, offset):
                nonlocal max_match_length, cumulative_match_length
                letter_to_check = inword[starting_pos_in_word + offset]
                letter_index = all_letters.index(letter_to_check)
                next_trie_node = current_trie_node.children[letter_index]
                if next_trie_node is not None:
                    cumulative_match_length += 1
                    if next_trie_node.terminus:
                        max_match_length = cumulative_match_length
                    if len(inword) > starting_pos_in_word + offset + 1:
                        recur_search_trie(next_trie_node, offset + 1)
                else:
                    return

            recur_search_trie(current_trie_node=trie_root_node, offset=0)
            result = inword if max_match_length == 0 else \
                inword[0:starting_pos_in_word] + \
                '[' + inword[starting_pos_in_word: (starting_pos_in_word + max_match_length)] + ']' + \
                inword[starting_pos_in_word + max_match_length:]

            return max_match_length, result

        # Attempt to match from each position in 'inword', from beginning to end.
        for starting_pos in range(len(inword)):
            trie_length, trie_outword = search_trie_from_word_pos(starting_pos)
            if trie_length > longest_match_for_word:
                longest_match_for_word = trie_length
                result = trie_outword

        return result

    # Create trie for 'parts' variable. 
    trie_root_node = TreeNode()
    for part in parts:
        add_part_to_trie(part, trie_root_node)

    # Process all words.
    result = []
    for word in words:
        result.append(process_word(word))

    return result


if __name__ == '__main__':
    ans = findSubstrings(#["Orange"],
                         ["Apple", "Melon", "Orange", "Watermelon"],
                         ["a", "mel", "lon",  "el",  "An"])
    print(ans)