import { configureStore } from '@reduxjs/toolkit';
import backgroundReducer from './background/background.reducer';
import itemLayoutReducer from "./item-layout/item-layout.reducer";

const store = configureStore({
    reducer: {
        background: backgroundReducer,
        item: itemLayoutReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
