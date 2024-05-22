<script lang="ts">
	import type { Team } from '../../types';
	import DataTable from './(components)/Table.svelte';

	export let teams: Team[] = [];

	teams = [
		{
			id: 2134,
			name: 'RH',
			services: [
				{
					name: 'Proxy'
				}
			]
		},
		{
			id: 23455634,
			name: 'UI/UX',
			services: [
				{
					name: 'Proxy'
				},
				{
					name: 'Git'
				}
			]
		},
		{
			id: 23456576,
			name: 'DevOps',
			services: []
		}
	];
</script>

<header class="mb-5">
	<h1 class="text-xl">Your organization's teams:</h1>
</header>
<DataTable {teams} />
