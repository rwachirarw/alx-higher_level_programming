#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted list
 * @head: head of the list
 * @number: data of the list
 * Return: a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	if (*head == NULL || head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	temp = *head;

	while (temp != NULL)
	{
		if ((number > temp->n) && (number < temp->next->n))
		{
			new_node->next = temp->next;
			temp->next = new_node;
			break;
		}
		temp = temp->next;
	}
	return (new_node);
}
