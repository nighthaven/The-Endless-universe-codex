import { configureStore } from '@reduxjs/toolkit';
import backgroundReducer from './background/background.reducer';

const store = configureStore({
    reducer: {
        background: backgroundReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
