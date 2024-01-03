#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head to the linked list.
 * @number: number to be inserted.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur;
	listint_t *tmp = (listint_t *)malloc(sizeof(listint_t));
	
	if (tmp == NULL)
	{
		perror("error in mallocing");
		return (NULL);
	}

	tmp->n = number;
	tmp->next = NULL;

	if (*head == NULL || (*head->n) >= number)
	{
		tmp->next = *head;
		*head = tmp;
	}
	else
	{
		cur = *head;

		while (cur->next != NULL && cur->next->n < number)
		{
			cur = cur->next;
		}
		tmp->next = cur->next;
		cur->next = tmp;
	}

	return (tmp);
}
