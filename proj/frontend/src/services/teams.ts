export const deleteTeam = async (teamId: string) => {
	const endpoint = `/api/teams/${teamId}`;

	const response = await fetch(endpoint, {
		method: 'DELETE'
	});

	return response;
};
