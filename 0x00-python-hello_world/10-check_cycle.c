#include "lists.h"

/**
 * check_cycle - check for list cycle
 * @n: first pointer
 * @p: second pointer
 * @list: list pointer
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *g;
	listint_t *p;

	g = list;
	p = list;

	while (g != NULL && p != NULL && p->next != NULL)
	{
		g = g->next;
		p = p->next->next;

		if (g == p)
		{
			return (1);
		}
	}
	return (0);
}
