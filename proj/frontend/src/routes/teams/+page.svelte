<script lang="ts">
	import type { LayoutData } from './$types';
	import DataTable from './(components)/Table.svelte';

	export let data: LayoutData;

	$: teams = data.teams;
</script>

<header class="mb-5">
	<h1 class="text-xl">Your organization's teams:</h1>
</header>
<DataTable {teams} />
