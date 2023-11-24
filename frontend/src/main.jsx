import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { ContextProvider } from './Components/Hooks/useStateContext';

const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
  });

ReactDOM.createRoot(document.getElementById("root")).render(
    <ContextProvider>
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
    <App />
    </ThemeProvider>
    </ContextProvider>
);