#include "lists.h"

/**
 * check_cycle - checks if their is a cycle in a linked list
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast	= NULL;
	listint_t *slow = NULL;

	if (!list)
		return (0);

	fast = list->next;
	slow = list;

	while (fast != slow)
	{
		if (fast->next == NULL || fast == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
