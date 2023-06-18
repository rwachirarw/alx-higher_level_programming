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

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	temp = *head;
	while (temp != NULL)
	{
		if (number < (*head)->n)
		{
			new_node->next = *head;
			*head = new_node;
			break;
		}
		if (temp->next == NULL)
		{
			temp->next = new_node;
			break;
		}

		if ((number == temp->n) || ((number > temp->n) && (number < temp->next->n)))
		{
			new_node->next = temp->next;
			temp->next = new_node;
			break;
		}

		temp = temp->next;
	}
	return (new_node);
}
