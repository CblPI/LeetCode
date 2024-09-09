import pytest

from structures.LIST import ListNode
from tasks.intersection_of_two_linked_lists import Solution


@pytest.mark.parametrize(
    "list1, list2, intersection_list, expected_intersection", [
        ([4, 1, 8, 4, 5], [5, 6, 1], [8, 4, 5], 8),
        ([4, 5], [5, 5], [512, 525], 512),
        ([4, 5], [5, 5], [512, 525], 512)
    ]
)
def test_intersection_of_two_linked_list(list1, list2, intersection_list, expected_intersection):
    node1 = ListNode()
    node1.fill(list1)

    node2 = ListNode()
    node2.fill(list2)

    intersection_node = ListNode()
    intersection_node.fill(intersection_list)

    last_node_list1 = node1
    while last_node_list1.next:
        last_node_list1 = last_node_list1.next
    last_node_list1.next = intersection_node

    last_node_list2 = node2
    while last_node_list2.next:
        last_node_list2 = last_node_list2.next
    last_node_list2.next = intersection_node

    intersection_result = Solution.getIntersectionNode(node1, node2)
    assert intersection_result.val == expected_intersection