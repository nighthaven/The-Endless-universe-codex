import { RootState } from '../store';

const selectFireflies = (state: RootState) => state.background.fireflies;

export default selectFireflies;
