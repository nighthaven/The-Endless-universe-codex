'use client';

import { motion } from 'framer-motion';
import clsx from 'clsx';
import { ReactNode, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../store/store';
import {
  showItem,
  hideItem,
} from '../../store/item-layout/item-layout.reducer';

interface ItemLayoutProps {
  children: ReactNode;
  // eslint-disable-next-line react/require-default-props
  className?: string;
  // eslint-disable-next-line react/require-default-props
  disableAnimation?: boolean; // Nouvelle prop
}

function ItemLayoutComponent({
  children,
  className,
  disableAnimation,
}: ItemLayoutProps) {
  const dispatch = useDispatch();
  const isVisible = useSelector((state: RootState) => state.item.visible);

  useEffect(() => {
    if (!disableAnimation) {
      dispatch(showItem());
    }

    return () => {
      if (!disableAnimation) {
        dispatch(hideItem());
      }
    };
  }, [dispatch, disableAnimation]);

  const scaleValue = disableAnimation || isVisible ? 1 : 0;

  return (
    <motion.div
      initial={{ scale: disableAnimation ? 1 : 0 }}
      animate={{ scale: scaleValue }}
      transition={{ duration: disableAnimation ? 0 : 0.5 }}
      className={clsx(
        'custom-bg p-6 sm:p-8 rounded-xl flex items-center justify-center space-y-8',
        className
      )}
      data-testid="item-layout"
    >
      {children}
    </motion.div>
  );
}

export default ItemLayoutComponent;
