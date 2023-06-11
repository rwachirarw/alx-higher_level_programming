#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of a linked list
 * Return: 1 if palindrome, 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = NULL, *fast = NULL, *prev = NULL, *tmp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	if (fast)
		slow = slow->next;

	while (prev && slow)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
