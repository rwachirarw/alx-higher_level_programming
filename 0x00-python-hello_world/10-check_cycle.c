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

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != slow)
	{
		slow = slow->next;
		fast = fast->next;
		if (!fast->next)
			return (0);
		fast = fast->next;
		if (!fast->next)
			return (0);
	}
	return (1);
}
