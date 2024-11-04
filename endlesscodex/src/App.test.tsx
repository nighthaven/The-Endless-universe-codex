import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

test('renders App component', () => {
  const { getByText } = render(<App />);
  expect(getByText(/some text in App component/i)).toBeInTheDocument();
});
