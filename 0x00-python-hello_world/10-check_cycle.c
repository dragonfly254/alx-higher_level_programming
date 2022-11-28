#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle within.
 * @list: singly linked list.
 *
 * Return: 0 is there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (!list)
		return(0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		tail = tail->next;
		if (tail == head)
			return (1);
	}

	return (0);
}
