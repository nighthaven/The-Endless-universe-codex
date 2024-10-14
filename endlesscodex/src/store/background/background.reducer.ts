import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Firefly {
    id: number;
    top: string;
    left: string;
    animationDuration: string;
}

interface BackgroundState {
    fireflies: Firefly[];
}

const initialState: BackgroundState = {
    fireflies: [],
};

const backgroundSlice = createSlice({
    name: 'background',
    initialState,
    reducers: {
        addFirefly: (state, action: PayloadAction<Firefly>) => {
            if (state.fireflies.length >= 14) {
                state.fireflies.shift();
            }
            state.fireflies.push(action.payload);
        },
    },
});

export const { addFirefly } = backgroundSlice.actions;
export default backgroundSlice.reducer;
