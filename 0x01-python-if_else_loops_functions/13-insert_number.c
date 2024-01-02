#include <stdlib.h>
#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: head of the linked list.
 * @number: number to insert.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur;
	listint_t *prev;
	listint_t *tmp = malloc(sizeof(listint_t));

	if (!tmp)
		return (NULL);

	if (*head == NULL)
	{
		tmp->n = number;
		*(head) = tmp;
		tmp->next = NULL;
	}

	cur = *(head);
	prev = *(head);

	if (cur->n > number)
	{
		tmp->n = number;
		tmp->next = cur;
		*(head) = tmp;
	}

	while (cur)
	{
		if (cur->n > number)
		{
			tmp->n = number;
			prev->next = tmp;
			tmp->next = cur;

			return tmp;
		}
		prev = cur;
		cur = cur->next;
	}
	prev->next = tmp;
	tmp->n = number;
	tmp->next = NULL;
	return (tmp);
}
