#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of singly linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *lug;
	listint_t *lead;

	if (list == NULL)
		return (0);

	if (list->next == NULL)
		return (0);

	lug = list;
	lead = list->next;

	while (lead != NULL && lead->next != NULL)
	{
		if (lug == lead)
			return (1);

		lug = lug->next;
		lead = lead->next->next;
	}

	return (0);
}
