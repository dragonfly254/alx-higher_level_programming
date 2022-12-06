#include "lists.h"

/**
 * reverse_list - reverses a given list.
 * @head: start of the list.
 *
 * Return: NULL if failed, head if successful.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *p, *q;

	if (head == NULL)
		return NULL;

	p = head;
	q = p->next;

	if (q == NULL)
		return NULL;

	q = reverse_list(q);
	p->next->next = p;
	p->next = NULL;

	return (q);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fp, *sp, *sec_start;

	if (*(head) == NULL)
		return (1);

	fp = *(head);
	sp = *(head);

	while (true)
	{
		fp = fp->next->next;
		if (fp->next == NULL)
		{
			sec_start = sp->next->next;
			break;
		}
		if (fp == NULL)
		{
			sec_start = sp->next;
			break;
		}
		sp = sp->next;
	}
	sp->next = NULL;

	listint_t *nsec_head = reverse_list(sec_start), *f_start = *(head);

	while (f_start && nsec_start)
	{
		if (f_start->n != nsec_start->n)
			return (0);
		f_start = f_start->next;
		nsec_start = nsec_start->next;
	}
	
	return (1);
}
