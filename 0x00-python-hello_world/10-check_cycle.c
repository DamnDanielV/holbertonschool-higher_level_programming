#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the linked lost head
 * Return: 0 (no cycle), 1 if (is a cicle)
 */
int check_cycle(listint_t *list)
{
	listint_t *l, *f;
    int r = 0;
	if (list == NULL)
		return (r);
	l = list;
	f = list;
	while (f->next->next && f->next)
	{
		l = l->next;
		f = f->next->next;
		if (l == f)
			r = 1;
	}
	return (r);
}
