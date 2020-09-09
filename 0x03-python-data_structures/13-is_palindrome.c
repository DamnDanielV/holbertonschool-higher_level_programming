#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i = 0, temp_array, len, x = 0, re = 1, co;
	int array[10];
	listint_t *tmp = *head;

	while (tmp)
	{
		array[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	len = 10;
	for (x = 0; x < len / 2; x++)
	{
		temp_array = array[x];
		array[x] = array[len - 1 - x];
		array[len - 1 - x] = temp_array;
	}
	co = 9;
	i = 0;
	while (i < 10 && co >= 0)
	{
		if (array[i] != array[co])
			return (0);
		i++;
		co--;
	}
	return (re);
}
