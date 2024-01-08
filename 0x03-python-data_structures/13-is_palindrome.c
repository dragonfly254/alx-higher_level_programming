#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of linked lists.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int *arrptr = NULL;
	int i, length = 0;
	listint_t *cur = NULL;

	cur = *head;

	while (cur)
	{
		length++;
		cur = cur->next;
	}

	arrptr = (int *)malloc(sizeof(int) * length);

	cur = *head;
	i = 0;

	while (cur)
	{
		arrptr[i] = cur->n;
		cur = cur->next;
		i++;
	}

	i = 0;
	length--;

	while (i < length)
	{
		if (arrptr[i] != arrptr[length])
		{
			return (0);
		}
		i++;
		length--;
	}
	free(arrptr);

	return (1);
}
