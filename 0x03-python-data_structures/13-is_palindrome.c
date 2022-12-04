#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur;
	int s_idx, e_idx, len = 0;
	if (*(head) == NULL)
		return (1);

	cur = *(head);
	while (cur)
	{
		len++;
		cur = cur->next;
	}
	cur = *(head);
	int i = 0, arr[len];
	for (i; cur; i++)
	{
		arr[i] = cur->n;
		cur = cur->next;
	}

	s_idx = 0;
	e_idx = len - 1;
	while (s_idx != e_idx)
	{
		if (arr[s_idx] != arr[e_idx] && s_idx <= len / 2)
			return (0);
		s_idx++;
		e_idx--;
	}

	return (1);
}
