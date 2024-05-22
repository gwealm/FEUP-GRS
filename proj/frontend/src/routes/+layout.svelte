<script>
	import '../app.css';

	import { Toaster } from '$lib/components/ui/sonner';

	import Header from './(components)/Header.svelte';
</script>

<Header />
<main class="flex flex-1 flex-col p-20">
	<slot />
</main>
<Toaster />
