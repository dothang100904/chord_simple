def test_lookup():
    node_ids = [1, 4, 8, 12]
    nodes = [Node(nid) for nid in node_ids]
    
    test_cases = [
        (0, 1),
        (2, 4),
        (5, 8),
        (10, 12),
        (13, 1),
        (15, 1),
    ]

    passed = 0
    for key, expected in test_cases:
        succ = find_successor(key, nodes)
        print(f"Testing key {key} → expected successor: {expected}, got: {succ.id}")
        assert succ.id == expected, f" Key {key} → Expected {expected}, got {succ.id}"
        passed += 1

    print(f" {passed}/{len(test_cases)} test cases passed!")

test_lookup()